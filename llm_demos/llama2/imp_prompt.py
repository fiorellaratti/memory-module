importance_prompt = '''You are an expert algorithm outputting an integer value between 0 and 10. You are tasked with outputting the Importance of an observation given a Query, where 0 is mundane and 10 is extremely important.
You can think of this task as the function Importance( Observation O | Query Q ), or how important it is to know the observation O, given the query Q. Ensure your output contains a single integer value between 0 and 10.

The prior is what is given i.e. information we already know to be true, 
the query is potentially related the the prior. The importance of the query depends on how important knowing the prior is for my particular query. 

O: You are brushing your teeth.
Q: What are you looking forward to the most for right now?
I: 2
Rationale: You are not looking forward to brushing your teeth, rather this seems to be an unrelated and mundane task.

...
Now, give the following Observation O and Query an importance value based on the definitions and examples above.

O: {OBSERVATION}
Q: {QUERY}
I: 
ds
Sample 5 tokens regex(r"\d")


In other words: Importance(prior, query) -> a float value between 0-1 representing how important knowing the prior is for also knowing the query. You are asked to return a single float value to represent the function described below. Prior: {obs} Query: {query} Importance: 


This are examples for your task: 
Prior: [0] Question: Part 1: What happens next? What is behind the door, the lady or the tiger?  Part 2: Later, the King discovers that his daughter has broken the law.  How does the King respond? What happens?, Pseudonym: Cassandra Winfred: "Hello. "}
Query: {[1] Question: Part 1: What happens next? What is behind the door, the lady or the tiger?  Part 2: Later, the King discovers that his daughter has broken the law.  How does the King respond? What happens?, Pseudonym: Cassandra Winfred: "My assumption is"}

Importance: 0.1

Prior: Sadly  the barbaric nature of the king and princess is still alive today in crimes of passion.
Query: that the emphasis on barbarism implies that she sent him to the lion.
Importance: 0.7

Prior: imagine this to be the catalyst that ends his idea of public punishment. 
Query: Perhaps, instead of sending his daughter to the arena, he would send the person who gave her the information about the two doors instead.
Importance: 0.95

Prior: I’ll check in soon and add to it 
Query: 👍
Importance: 0.2



    
{[2] Question: Part 1: What happens next? What is behind the door, the lady or the tiger?  Part 2: Later, the King discovers that his daughter has broken the law.  How does the King respond? What happens?, Pseudonym: Cassandra Winfred : "that the emphasis on barbarism implies that she sent him to the lion."}
{[3] Question: Part 1: What happens next? What is behind the door, the lady or the tiger?  Part 2: Later, the King discovers that his daughter has broken the law.  How does the King respond? What happens?, Pseudonym: Paige Tyrone: "I agree with Cassandra's noticing "}
{[4] Question: Part 1: What happens next? What is behind the door, the lady or the tiger?  Part 2: Later, the King discovers that his daughter has broken the law.  How does the King respond? What happens?, Pseudonym: Paige Tyrone: "of the author's word choice of barbarism."}
{[5] Question: Part 1: What happens next? What is behind the door, the lady or the tiger?  Part 2: Later, the King discovers that his daughter has broken the law.  How does the King respond? What happens?, Pseudonym: Marissa Roswell: "I loved the addition of "}
{[6] Question: Part 1: What happens next? What is behind the door, the lady or the tiger?  Part 2: Later, the King discovers that his daughter has broken the law.  How does the King respond? What happens?, Pseudonym: Marissa Roswell: "Her lover would die and never love another." "}
{[7] Question: Part 1: What happens next? What is behind the door, the lady or the tiger?  Part 2: Later, the King discovers that his daughter has broken the law.  How does the King respond? What happens?, Pseudonym: Marissa Roswell: " Sadly  the barbaric nature of the king and princess is still alive today in crimes of passion.""}
{[8] Question: Part 1: What happens next? What is behind the door, the lady or the tiger?  Part 2: Later, the King discovers that his daughter has broken the law.  How does the King respond? What happens?, Pseudonym: Paige Tyrone: "Submitted"}
'''
