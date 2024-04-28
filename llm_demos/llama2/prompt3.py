question_prompt = '''Take on the role of a classification task for a given input context and message. 

Given: a topic, context and message. The topic is what the students are discussing. The context are important messages related to the message you will be classifying. The message is the one you need to classify, it will have the format of {[Index] Pseudonym: "Message"}
Task: give the message an appropriate Question Class.

Description: You will be classifying a message from students discussing a certain topic. Each message can only have one question class or it can be None if no question is identified.
Example Output:

 ```json
{
    "question": "...question classification", 
    "rationale": "Reason for question classification"
}
 ```
# Question types:
## O-LOT:
- Definition: Questions that are open-ended, but involve lower-order thinking.
- Example Usage: So when you read this, what did you think?

## C-LOT:
- Definition: Questions that are closed-ended, lower-order. thinkingi--that is, questions for which there is an answer in mind.
- Example Usage: Are we supposed to write out answer in the text box below?

## None:
- No question identified.

# Example Input/Outputs for your output in this task.
## Example 1:
### Input:
 - Topic: The book "The lady or the tiger" by Frank R. Stockton
 - Context: {[1] Cassandra Winfred: "My assumption is"}, {[2] Cassandra Winfred : "that the emphasis on barbarism implies that she sent him to the lion."},
 - Message: "{[0] Cassandra Winfred: "Hello. "}"

### Output:
```json
{
    "question": "None",
    "rationale": "Hello is not a question"

}
```
## Example 2:
### Input:
 - Topic: The book "The lady or the tiger" by Frank R. Stockton
 - Context: {[17] Cheryl Diaz: "Hi. I'm not sure if we were supposed to ultimately write an ending to the story or just answer the prompts collectively. I wrote an ending below, and you can change it or replace it. We just want to test the use of the space at the same time, I think.", {[18] Cheryl Diaz: "Do you see what I typed in the box below?",[23] Deborah Evans: "Good luck to you as well"
 - Message: "{[22] Deborah Evans :"Looks good! I guess we can complete the post survey and submit our assignment"}"

### Output:
```json
{
    "question": "None",
    "rationale": "No question was asked."
}
```
## Example 3:
### Input:
 - Topic: The book "The lady or the tiger" by Frank R. Stockton
 - Context: No context
 - Message: "{[17] Patricia Green: "How much longer would you like to wait for Julie before we begin? 5 more minutes?"}"

### Output:
```json
{
    "question": "C-LOT",
    "rationale": "There is a question in the message classified as C-LOT because it is not related to the topic."
}
```

# Classification
Task: Given the Topic, Context and Message, classify the message with an appropriate Question Class. 

Remember, your task is to only classify the given message. Here are the possible question classes: O-LOT, C-LOT.

Please classify the following message and nothing else to get points: 
## Input:
 - Topic: $TOPIC$
 - Context: $CONTEXT$
 - Message: "$MESSAGE$"'''