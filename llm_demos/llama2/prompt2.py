uptake_prompt = '''Take on the role of a classification task for a given input context and message. 

Given: a topic, context and message. The topic is what the students are discussing. The context are important messages related to the message you will be classifying. The message is the one you need to classify, it will have the format of {[Index] Pseudonym: "Message"}
Task: give the message an appropriate Uptake Class.

Description: You will be classifying a message from students discussing a certain topic. Each message can only have one uptake class or it can be None if no uptake is identified.
Example Output:

 ```json
{
    "uptake": "...uptake classification", 
    "rationale": "Reason for uptake classification"
}
 ```

# Uptake types:

## Affirm:
- Definition: The action or process of affirming something or being affirmed, showing agreement.
- Example Usage: That’s a good point. I agree.

## Elaborate:
- Definition: Provide additional examples, detail or explanation. These are statement, NOT questions or commands.
- Example Usage: Another example of this….

## Clarify:
- Definition: Ask questions or make commands, to improve comprehension.
- Example Usage: So you are saying…? Do you mean…?.

## Disagree:
- Definition: To express a differing opinion.
- Example Usage: I disagree. This means something different than what you stated.

## Prompt:
- Definition: Refers back and responds to a previous discussion or question.
- Example Usage: Going back to your previous question….

## Filler:
- Definition: Acknowledges the previous person’s position without adding anything of substance to the conversation; a comment made for the purpose of satisfying participation grade requirements.
- Example Usage: (No example provided)

## Respond:
- Definition: Answer a previous question or make a decision based on a question.
- Example Usage: In response to “okay should we start writing about it or should we find some quotes first and talk about them?” someone says, “find quotes first.”

##None:
- No uptake identified.

# Example Input/Outputs for your output in this task.
## Example 1:
### Input:
 - Topic: The book "The lady or the tiger" by Frank R. Stockton
 - Context: {[1] Cassandra Winfred: "My assumption is"}, {[2] Cassandra Winfred : "that the emphasis on barbarism implies that she sent him to the lion."},
 - Message: "{[0] Cassandra Winfred: "Hello. "}"

### Output:
```json
{
    "uptake": "None",
    "rationale": "There is no uptake identified in the message"

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
    "uptake": "Affirm",
    "rationale": "Uptake for the message would be Affirm since something is being affirmed."
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
    "uptake": "Clarify",
    "rationale": "The uptake will be clarified since it is asking a clarifying question."
}
```

# Classification
Task: Given the Topic, Context and Message, classify the message with an appropriate Uptake Class. 

Remember, your task is to only classify the given message. Here are the possible uptake classes: Affirm, Elaborate, Clarify, Disagree, Prompt, Filler, Respond.

Please classify the following message and nothing else to get points: 
## Input:
 - Topic: $TOPIC$
 - Context: $CONTEXT$
 - Message: "$MESSAGE$"'''