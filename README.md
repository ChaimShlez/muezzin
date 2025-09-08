#  muezzin


## data-loader

* Extracting metadata from a folder containing podcasts audio files (size,path,creation-time,last modified).
* Connecting to Kafka and sending to topic : metadata_podcasts.
* There is a manager who is responsible for running all stages and is responsible for the order of operations.


## data-distribution

### This department's job is to distribute the information to the database.

* Taking the data from the appropriate topic in Kafka
* Skipping one record after another (because the consumer is listening all the time)
* Creating a unique id for each record by entering it into a hash function 
* (I only took part of the generated text because it is very long and was not necessary)
* I took the path of each file and transcribed it using the "faster_whisper" package, which is an optimization for openAI's whisper,
and I chose to do the transcription already at this stage because I saw no reason to make unnecessary api calls to get the binary file stored in Mongo
if I already have the path of the file.
* I save the metadata in Elastic with the text and the id, 
* I converted the file contents to binary with "bson.binary" and I save it with the id in Mongo




