# LOGSHAPER-OOBAtoDPO
LOGSHAPER is an initiative to take all of the work I've done in [OOBA](https://github.com/oobabooga/text-generation-webui) and convert those interactions to trainable formats. This python script changes the first and second message in your logs to the "question" and "rejected" fields of DPO format.


Step 1: Change the string in line 23 to your folder

Step 2: Change the string in line 24 to an output file in jsonl of your choice

Step 3: From your IDE or in your terminal, run the python script. For Linux it will look something like `python3 dpo.py` and in Windows it will be `python dpo.py`

Step 4: Write the "system" and "chosen" for each point in the newly created dataset.
