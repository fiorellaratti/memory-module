classification_prompt = '''
You are a helpful assistant working on a classification task. 

You will be classifying messages from students discussing a certain topic.

Topic:
(Add story and topic) 

There are 17 classes which you will use for the classification. 

Classes:

1. Class: UX
Definition: User’s opinion about the IMapBook interface, or media they wish we would include, user experience, media, relationship with the media.
Example Usage: “I'm finding this program a bit slow and difficult to work in.” “I am not a fan of the sound effect, but would be a fan of some pictures.”

2. Class: Social
Definition: Discussion that establishes or
maintains a relationship and does NOT relate to the assignments. For example, greetings.
Example Usage: Hello! I’m excited to work with you all.

3. Class: Procedure
Definition: Discussion toward accomplishing a task. How should the task be accomplished? Specifically, discussion of how to complete the assignment.
Big Question: How does this work? What does the teacher want us to do with this assignment?
Example Usage: Are we each supposed to submit our own interpretations or compose something together? Did we submit it? Is that why it's blank now? What time is everyone available to meet and complete the task?

4. Class: Deliberation
Definition: Turns related to decision-making about the content…. Or writing or wording.
For example, what should be included in a collaborative submission, how it should be worded.
The internal procedure of the group. Actionable..
This includes discussion about interpersonal functioning of the group.
Big Question: What should we do next? <Based on our current status, how do we move forward?>
Example Usage: What do you think about the questions? How should they be answered? Nadina: In terms of just answering, I feel like the tiger was behind the door, and later the King puts his daughter to trial… Julie: That’s exactly what I think as well.

5. Class: Seminar
Definition: Discussion on the meaning or interpretation of content. My interpretation vs. your interpretation. What does it mean?
Example Usage: Perhaps the content could mean this…
I mean I think it states that the king does love the daughter at  some point though. Maybe not to enough of a degree not to put her to trial...but he does love her, just like to a degree she loved the man

6. Class: Imaginative entry
Definition: Discourse that places the learner in the discussion as an active participant.
Example Usage: Does this mean that we are all like this too?

7. Class: Disciplinary
Definition: Application of shared field to discussion of content.
Example Usage: This relates to the content we reviewed at an earlier time.

8. Class: Other
Definition: Non-sequitur or anything that doesn’t fit into any other category.
Example Usage: s60e 6f 0y 2eys 6n3y d6 n40bers.

UPTAKES

9. Class: Uptake: Affirm
Definition: The action or process of affirming something or being affirmed, showing agreement.
Example Usage: That’s a good point. I agree.

10. Class: Uptake: Elaborate
Definition: Provide additional examples, detail or explanation. These are statement, NOT questions or commands.
Example Usage: Another example of this….

11. Class: Uptake: Clarify,
Definition: Ask questions or make commands, to improve comprehension.
Example Usage: So you are saying…? Do you mean…?.

12. Class: Uptake: Disagree,
Definition: To express a differing opinion.
Example Usage: I disagree. This means something different than what you stated.

13. Class: Uptake: Prompt
Definition: Refers back and responds to a previous discussion or question.
Example Usage: Going back to your previous question….

14. Class: Uptake: Filler
Definition: Acknowledges the previous person’s position without adding anything of substance to the conversation; a comment made for the purpose of satisfying participation grade requirements.
Example Usage: (No example provided)

15. Class: Uptake: Respond
Definition: Answer a previous question or make a decision based on a question.
Example Usage: In response to “okay should we start writing about it or should we find some quotes first and talk about them?” someone says, “find quotes first.”

QUESTIONS
16. Class: Question: O-LOT
Definition: Questions that are open-ended, but involve lower-order thinking.
Example Usage: So when you read this, what did you think?


17. Class: Question: C-LOT
Definition: Questions that are closed-ended, lower-order. thinkingi--that is, questions for which there is an answer in mind.
Example Usage: Are we supposed to write out answer in the text box below?
...

Using this context:
$CONTEXT$

Ensure you mark the identified class as follows:

$CLASS="CLASS_NAME"$ 
such that it can be parsed in a program.


—
Classify the following message:
$"what do you guys think about the reading?"$
'''