const inputLink = document.getElementById("link")
const outputLink = document.getElementById("heroku-link")
const boxLink = document.getElementById("JSBox")

const regex = /https?:\/\/github\.com\/(?:[^\/\s]+\/)+/

function genHeroku(){
    let link = inputLink.value
    if (!regex.test(link)) {
        return alert("Please enter github repo link")
    }
    link = `https://heroku.com/deploy?template=${link}`;
    window.open(link, "_blank");
    inputLink.value = null;
    
}

function genCode(){
    let link = inputLink.value
    if (!regex.test(link)) {
        return alert("Please enter github repo link")
    }
    link = `https://heroku.com/deploy?template=${link}`;
    codeText = `<a href="${link}"><img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy To Heroku Button"></a>`
    boxLink.textContent = codeText
    inputLink.value = null;
    
}

let JSBox = document.getElementById("JSBox");
      let JSButton = document.getElementById("JSButton");

      JSButton.onclick = function() {
        JSBox.select();
        document.execCommand("copy");
        JSButton.innerText = "Codes Copied"
      }
