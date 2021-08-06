const container1=document.querySelector(".container1");
const toggleList = document.querySelector(".toggleList");
const moreInfo = document.querySelector(".moreInfo");


container1.addEventListener("click", (event)=>{
    if(event.target.tagName == "H1"){
        event.target.textContent = "Have a Good Time!";
    }
})


toggleList.addEventListener("click", () =>{
    if (toggleList.textContent === "Show More"){
        toggleList.textContent = "Hide"
        moreInfo.style.display="block"
    } else if (toggleList.textContent === "Hide") {
        toggleList.textContent = "Show More"
        moreInfo.style.display="none"
    } 
} )
