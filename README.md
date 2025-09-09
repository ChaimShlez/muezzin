#  muezzin


## data-loader

* Extracting metadata from a folder containing podcasts audio files (size,path,creation-time,last modified).
* Connecting to Kafka and sending to topic : metadata_podcasts.
* There is a manager who is responsible for running all stages and is responsible for the order of operations.


## data-distribution

### This department's job is to distribute the information to the database.

* Taking the data from the appropriate topic in Kafka
* Skipping one record after another (because the consumer is listening all the time)
* Creating a unique ID for each record by feeding it to a hash function
* (I only took a part of the generated text because it is very long and was not needed)
* I store the metadata in Elastic with the text and the ID,
* I converted the file content to a binary file with "bson.binary" and I store it with the ID in Mongo
* I added only the ID to another topic, and then used another service to retrieve the IDs and pull them from Mongo.
* The reason I chose to do this is because it is a time-consuming process and I did not want it to delay the metadata being sent.
* Kafka also helps me maintain order because it works in a queue, and even if the system crashes, I can easily know where I stopped the transcription.
* I extracted from a binary file using o.BytesIO which takes the binary string and puts it into a file that can be read from it and the transcription library knows how to read the file.
* And I transcribed it using the "faster_whisper" package, which is an optimization for openAI's whisper,
