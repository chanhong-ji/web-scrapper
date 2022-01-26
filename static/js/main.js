const header = document.querySelector("header");
const form = header.querySelector("form");
const input = form.querySelector("input");
const tagList = header.querySelector("ul");
const tagNode = tagList.querySelectorAll("li");
let tags = JSON.parse(localStorage.getItem("tags")) || [];

function onTagClick(event) {
  const keyword = event.target.innerHTML.slice(1);
  window.location.href = `/search?keyword=${keyword}`;
}

function paintTags() {
  tagList.innerHTML = "";
  for (let tag of tags) {
    li = document.createElement("li");
    li.innerText = "#" + tag;
    tagList.append(li);
  }
  const tagListTag = tagList.querySelectorAll("li");
  tagListTag.forEach((tag) => tag.addEventListener("click", onTagClick));
}

paintTags();

function onScroll() {
  if (window.scrollY > 100) {
    form.style.paddingTop = "50px";
  } else {
    form.style.paddingTop = "100px";
  }
}

window.addEventListener("scroll", onScroll);

function saveTags() {
  localStorage.setItem("tags", JSON.stringify(tags));
}

function onFormSubmit() {
  const value = String(input.value).toLowerCase().trim();
  if (tags.length > 5) {
    tags.shift();
  }
  tags.push(value);
  saveTags();
}

form.addEventListener("submit", onFormSubmit);
