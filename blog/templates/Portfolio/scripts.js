var myList = document.getElementById("list");
var btn1 = document.getElementById("btn1");
var btn2 = document.getElementById("btn2");
var story = document.getElementsByClassName("item-button");
var popup = document.getElementsByClassName("popup")[0];
var close = document.querySelector(".close");

function addItem(){
    var newList = document.createElement("li");
    newList.innerHTML = "Добавить новость";
    newList.className = "item-button";
    myList.appendChild(newList);
    popup.style.display = "none";
}


function delItem(){
    myList.removeChild(story[0]);

    if(story.length == 0){
        popup.style.display = 'block';
    }
}

function closePopup(){
    popup.style.display = "none";
}

btn1.addEventListener("click", addItem);
btn2.addEventListener("click", delItem);
close.addEventListener("click", closePopup);
