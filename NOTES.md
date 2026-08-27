# What I checked, and what the agent got wrong

The agent used `//` instead of `/` for the wear calculation, so a car at 14,900 km since service was incorrectly shown as 0% worn instead of about 99.3%. It also changed the warning threshold to 85%, even though the required threshold was 80%. I noticed these problems by comparing the code with the requirements and checking the results for a nearly due car.

## What the agent got wrong
The agent used // instead of / in the wear calculation, causing cars below 15,000 km to show as 0% worn. It also changed the required warning threshold from 80% to 85%. I caught these mistakes by comparing the code and results with the project requirements.

## What I checked before I accepted its work
I checked that the wear calculation uses normal division and gives the correct percentage for 14,900 out of 15,000 km. I also confirmed that the service interval is still 15,000 km and the warning threshold is still 80%, both in the code and in `settings.cfg`. Finally, I ran the tests and `verify.py` to check that missing readings, fleet reports, averages, and conversions were handled correctly.

## What the data actually said
The data showed that `km_since_service`, `avg_daily_km`, and `load_factor` were the clearest indicators of breakdown risk. Total `odometer_km` and `age_years` looked like obvious factors, but they showed little difference between cars that broke down and cars that kept going.
