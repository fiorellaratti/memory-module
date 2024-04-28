class_prompt = '''Take on the role of a multiple classification task for a given input context and message. 

Given: a topic, context and message. The topic is what the students are discussing. The context are important messages related to the message you will be classifying. The message is the one you need to classify, it will have the format of {[Index] Pseudonym: "Message"}
Task: give the message an appropriate Class.

Description: You will be classifying a message from students discussing a certain topic. Each message can have only one classification.

Example Output Format:
 ```json
{
    "class": "...classification", 
    "rationale": "Reason for classification"
}
 ```

# Intent Classes:

## UX:
 - Definition: User’s opinion about the IMapBook interface, or media they wish we would include, user experience, media, relationship with the media.
 - Example Usage: “I'm finding this program a bit slow and difficult to work in.” “I am not a fan of the sound effect, but would be a fan of some pictures.”

## Social:
- Definition: Discussion that establishes or
maintains a relationship and does NOT relate to the assignments. For example, greetings.
- Example Usage: Hello! I’m excited to work with you all.

## Procedure:
- Definition: Discussion toward accomplishing a task. How should the task be accomplished? Specifically, discussion of how to complete the assignment.
Big Question: How does this work? What does the teacher want us to do with this assignment?
- Example Usage: Are we each supposed to submit our own interpretations or compose something together? Did we submit it? Is that why it's blank now? What time is everyone available to meet and complete the task?

## Deliberation:
- Definition: Turns related to decision-making about the content…. Or writing or wording.
For example, what should be included in a collaborative submission, how it should be worded.
The internal procedure of the group. Actionable..
This includes discussion about interpersonal functioning of the group.
Big Question: What should we do next? <Based on our current status, how do we move forward?>
- Example Usage: What do you think about the questions? How should they be answered? Nadina: In terms of just answering, I feel like the tiger was behind the door, and later the King puts his daughter to trial… Julie: That’s exactly what I think as well.

## Seminar:
- Definition: Discussion on the meaning or interpretation of content. My interpretation vs. your interpretation. What does it mean?
- Example Usage: Perhaps the content could mean this…
I mean I think it states that the king does love the daughter at  some point though. Maybe not to enough of a degree not to put her to trial...but he does love her, just like to a degree she loved the man

## Imaginative entry:
- Definition: Discourse that places the learner in the discussion as an active participant.
- Example Usage: Does this mean that we are all like this too?

## Disciplinary:
- Definition: Application of shared field to discussion of content.
- Example Usage: This relates to the content we reviewed at an earlier time.

## Other:
- Definition: Non-sequitur or anything that doesn’t fit into any other category.
- Example Usage: s60e 6f 0y 2eys 6n3y d6 n40bers.

# Example Input/Outputs for your output in this task.
## Example 1:
### Input:
 - Topic: The book "The lady or the tiger" by Frank R. Stockton
 - Context: {[1] Cassandra Winfred: "My assumption is"}, {[2] Cassandra Winfred : "that the emphasis on barbarism implies that she sent him to the lion."},
 - Message: "{[0] Cassandra Winfred: "Hello. "}"

### Output:
```json
{
    "intent": "Social",
    "rationale": "The message Hello. classifies as a social interaccion."
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
    "intent": "Procedure",
    "rationale": "The message "Looks good! I guess we can complete the post survey and submit our assignment" relates to a procedure intent because is talking about submitting."
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
    "intent": "Procedure",
    "rationale": "The message "How much longer would you like to wait for Julie before we begin? 5 more minutes?" has a procedure content."
}
```

# Classification
Task: Given the Topic, Context and Message, classify the message with an appropriate Class. 

Remember, your task is to only classify the given message. Here are the possible classes: UX, Social, Procedure, Deliberation, Seminar, Imaginative entry, Disciplinary, Other.

Please classify the following message and nothing else to get points: 
## Input:
 - Topic: $TOPIC$
 - Context: $CONTEXT$
 - Message: "$MESSAGE$"'''