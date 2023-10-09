let container = document.getElementById("greeting");
let timeNow = new Date().getHours();
let greeting =
  timeNow >= 5 && timeNow < 12
    ? "Good Morning Nanashi"
    : timeNow >= 12 && timeNow < 18
    ? "Good Afternoon Nanashi"
    : "Good evening Nanashi";
container.innerHTML = `<h1>${greeting}</h1>`;