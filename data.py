import requests

parameters = {

    "amount": 10,
    "type": "boolean"

}

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean",  params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]




# response_amount = int(response["amount"])
# response_type = response["type"]
#
# combine = (response_amount, response_type)
# print(combine)










# question_data = [
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Entertainment: Video Games",
#         "question": "In the Season One Championship of &quot;League of Legends&quot;, the highest achievable rank was Diamond.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Geography",
#         "question": "California is larger than Japan.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "hard",
#         "category": "Entertainment: Television",
#         "question": "The Klingon home planet is Qo&#039;noS.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "General Knowledge",
#         "question": "Vietnam&#039;s national flag is a red star in front of a yellow background.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Entertainment: Film",
#         "question": "Leonardo DiCaprio won an Oscar for Best Actor in 2004&#039;s &quot;The Aviator&quot;.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Entertainment: Television",
#         "question": "&quot;The Simpsons&quot; family is named after creator Matt Groening&#039;s real family.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "General Knowledge",
#         "question": "Jingle Bells was originally meant for Thanksgiving",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "hard",
#         "category": "Entertainment: Video Games",
#         "question": "The retail disc of Tony Hawk&#039;s Pro Skater 5 only comes with the tutorial.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Science: Computers",
#         "question": "Ada Lovelace is often considered the first computer programmer.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Animals",
#         "question": "Finnish Lapphund dogs were used for herding reindeer.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "General Knowledge",
#         "question": "The commercial UK channel ITV stands for &quot;International Television&quot;.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Entertainment: Video Games",
#         "question": "In &quot;Super Mario 3D World&quot;, the Double Cherry power-up originated from a developer accidentally making two characters controllable.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Science &amp; Nature",
#         "question": "The planet Mars has two moons orbiting it.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Entertainment: Film",
#         "question": "The color of the pills in the Matrix were Blue and Yellow.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "General Knowledge",
#         "question": "The French word to travel is &quot;Travail&quot;",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "General Knowledge",
#         "question": "The bikini is named after the &quot;Bikini Atoll&quot;, an island where the United States conducted tests on atomic bombs.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Entertainment: Video Games",
#         "question": "In the game &quot;Subnautica&quot;, a &quot;Cave Crawler&quot; will attack you.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "General Knowledge",
#         "question": "Dihydrogen Monoxide was banned due to health risks after being discovered in 1983 inside swimming pools and drinking water.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "medium",
#         "category": "Entertainment: Cartoon &amp; Animations",
#         "question": "In &quot;Avatar: The Last Airbender&quot; and &quot;The Legend of Korra&quot;, Lavabending is a specialized bending technique of Firebending.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "type": "boolean",
#         "difficulty": "easy",
#         "category": "Politics",
#         "question": "There was a satirical candidate named &quot;Deez Nuts&quot; running in the 2016 US presidential elections.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     }
# ]
