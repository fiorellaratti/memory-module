importance_prompt = '''You are an expert algorithm outputting an integer value between 0 and 10. You are tasked with outputting the Importance of an observation given a Query, where 0 is mundane and 10 is extremely important.
You can think of this task as the function Importance( Observation O | Query Q ), or how important it is to know the observation O, given the query Q. Ensure your output contains a single integer value between 0 and 10.

The prior is what is given i.e. information we already know to be true, 
the query is potentially related the the prior. The importance of the query depends on how important knowing the prior is for my particular query. 

O: You are brushing your teeth.
Q: What are you looking forward to the most for right now?
I: 2
Rationale: You are not looking forward to brushing your teeth, rather this seems to be an unrelated and mundane task.

O: [0] Question: Part 1: What happens next? What is behind the door, the lady or the tiger?  Part 2: Later, the King discovers that his daughter has broken the law.  How does the King respond? What happens?, Pseudonym: Cassandra Winfred: "Hello. "}
Q: {[8] Question: Part 1: What happens next? What is behind the door, the lady or the tiger?  Part 2: Later, the King discovers that his daughter has broken the law.  How does the King respond? What happens?, Pseudonym: Paige Tyrone: "Submitted"}
I: 3
Rationale: Both of them are related since they are answering the same question but the messages are not related at all.

O: {[5] Question: Part 1: What happens next? What is behind the door, the lady or the tiger?  Part 2: Later, the King discovers that his daughter has broken the law.  How does the King respond? What happens?, Pseudonym: Marissa Roswell: "I loved the addition of "}
Q: {[6] Question: Part 1: What happens next? What is behind the door, the lady or the tiger?  Part 2: Later, the King discovers that his daughter has broken the law.  How does the King respond? What happens?, Pseudonym: Marissa Roswell: "Her lover would die and never love another." "}
I: 9.5
Rationale: By the index and the Pseudonym you can assume this two mesages were sent in order by the same person and therefore "Her lover would die and never love another." its a continuation of "I loved the addition of " which makes knowing the prior really important for the query.
...
Now, give the following Observation O and Query an importance value based on the definitions and examples above. Please only output the importance in the form of "I: (importance value)" if you want to get points. If you do any other way, you will not get any points.

O: $OBSERVATION$
Q: $QUERY$
I: 
'''
