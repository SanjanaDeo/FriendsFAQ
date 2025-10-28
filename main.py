def main():
    print("Hello from fastapi-project!")

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working!"}

class Question(BaseModel):
    question: str   

faq = {
    "when did friends first air": "September 22, 1994",
    "when did friends end": "May 6, 2004",
    "how many seasons of friends are there": "10 seasons",
    "how many episodes are there in total": "236 episodes",
    "where is friends set": "New York City",
    "who are the six main characters": "Rachel, Ross, Monica, Chandler, Joey, and Phoebe",
    "which coffee shop do the friends frequently visit": "Central Perk",
    "who is ross’s first wife": "Carol",
    "what is the name of ross and carol’s son": "Ben",
    "what is the name of ross and rachel’s daughter": "Emma",
    "what is the name of joey’s stuffed penguin": "Hugsy",
    "what is phoebe’s most famous song": "Smelly Cat",
    "which character is known for saying 'we were on a break!'": "Ross",
    "what does chandler do for a living": "He works in statistical analysis and data reconfiguration (later advertising)",
    "who was monica’s first serious boyfriend in the show": "Richard Burke",
    "what is monica’s biggest pet peeve": "Animals dressed as humans",
    "who was rachel supposed to marry in the pilot": "Barry",
    "what is joey’s famous catchphrase": "'How you doin’?'",
    "what are the names of phoebe’s triplets": "Frank Jr. Jr., Leslie, and Chandler",
    "what tv soap opera does joey star in": "Days of Our Lives",
    "what is the name of joey’s character on the soap": "Dr. Drake Ramoray",
    "what is the name of chandler and joey’s pet duck": "Duck",
    "which two characters end up married": "Chandler and Monica, Ross and Rachel (implied)",
    "what are the names of monica and chandler’s twins": "Erica and Jack",
    "which friend was a chef": "Monica",
    "which friend worked in fashion": "Rachel",
    "which friend is a paleontologist": "Ross",
    "what instrument does phoebe play": "Guitar",
    "what is janice’s famous catchphrase": "'Oh. My. God.'",
    "what does joey never share": "Food",
    "name the holiday armadillo episode about": "Ross teaching Ben about Hanukkah",
    "who dated a yeti": "Rachel (Danny the 'Yeti')",
    "who invented the game 'bamboozled'": "Joey",
    "which character famously hates thanksgiving": "Chandler",
    "what is chandler’s middle name": "Muriel",
    "what is rachel’s last name": "Green",
    "what is monica’s biggest fear in her relationship with chandler": "That he will change his mind about marriage",
    "where does phoebe get her name 'princess consuela banana hammock'": "She changes her name legally",
    "what does mike change his name to in response": "Crap Bag",
    "which character lived with a roommate named eddie": "Chandler",
    "who was joey’s agent": "Estelle Leonard",
    "what’s the name of chandler’s annoying coworker": "Bob",
    "who accidentally threw a woman’s wooden leg in a fire": "Chandler",
    "who was ross’s second wife": "Emily",
    "which friend has a twin sister": "Phoebe (her twin Ursula)",
    "what does joey keep in the freezer because he is scared of it": "The Shining book",
    "what is the name of the restaurant where monica works as head chef": "Alessandro’s (later Javu)",
    "what does joey say to get out of situations he doesn’t like": "'I gotta go' or 'How you doin’?'",
    "which character is a control freak and loves cleaning": "Monica",
    "what is the final scene of friends": "The group leaves Monica’s apartment for the last time to get coffee"
}


@app.post("/ask")
def ask_question(data : Question):
    user_question = data.question.lower() 

    if user_question in faq:
        print(faq)
        return {"answer": faq[user_question]}
    else:
        return {"answer": "I don't know."}

if __name__ == "__main__":
    main()
