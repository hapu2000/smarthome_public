## INPUTS
entity_id  = data.get('entity_id')
states = hass.states.get(entity_id)
current_level = states.attributes.get('white_value') or 0
start_level_pct = int(data.get('start_level_pct', current_level ))
end_level_pct = int(data.get('end_level_pct'))
transition = data.get('transition')

## CALCULATE PARAMETERS FOR LOOP, BASED ON TRANSITION TIME FOR FADE
transition_secs = (int(transition[:2])*3600 + int(transition[3:5])*60
                   + int(transition[-2:]))    # convert string to total secs'
step_pct  = 1
sleep_delay = abs(transition_secs/(end_level_pct - start_level_pct))

# If fading out the step_pct will be negative (decrement each iteration)

if end_level_pct < start_level_pct: step_pct = step_pct * -1


## DOES THE WORK ...

# Since we check for equality of new_level_pct and current_level_pct
# in each loop -  and break if !=, we must initialize new_level_pct
# to equal start_level_pct, and then set actual light white_value
# (a.k.a. current_level_pct) to equal start_level_pct.

new_level_pct = start_level_pct
data = { "entity_id" : entity_id, "white_value" : round(start_level_pct) }
hass.services.call('light', 'turn_on', data)
time.sleep(1)  # without delay,'hass.states.get' would not get the new value

while round(new_level_pct) != end_level_pct :     ## until we get to new level
    states = hass.states.get(entity_id)           ##  acquire status of entity
    current_level_pct = states.attributes.get('white_value') or 0
    if (round(current_level_pct) != round(new_level_pct)):
        logger.info('Exiting Fade In')                ## this indicates manual
        break;                                        ## intervention, so exit
    else :
        new_level_pct = new_level_pct + step_pct
        logger.info('Setting white_value of ' + str(entity_id) + ' from '
          + str(current_level_pct) + ' to ' + str(new_level_pct))
        if new_level_pct == 0 and end_level_pct == 0:
            data = { "entity_id" : entity_id }
            hass.services.call('light', 'turn_off', data)
        else:
            data = { "entity_id" : entity_id,
                    "white_value" : round(new_level_pct) }
            hass.services.call('light', 'turn_on', data)
        time.sleep(sleep_delay)


##  Some test json input for Services in Developer tools
##{
##  "entity_id": "light.your_light_name",
##  "start_level_pct": "0",
##  "end_level_pct": "100",
##  "transition": "00:00:19"
##}
