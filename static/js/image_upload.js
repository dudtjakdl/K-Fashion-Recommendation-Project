var submit = document.getElementById("submitButton");
submit.onclick = showImage; //Submit 버튼 클릭시 이미지 보여주기

function showImage() {
  var newImage = document.getElementById("image-show").lastElementChild;
  newImage.style.visibility = "visible";

  document.getElementById("image-upload").style.visibility = "hidden";

  document.getElementById("fileName").textContent = null; //기존 파일 이름 지우기
}

function loadFile(input) {
  var file = input.files[0];

  var name = document.getElementById("fileName");
  name.textContent = file.name;

  var newImage = document.createElement("img");
  newImage.setAttribute("class", "img");

  newImage.src = URL.createObjectURL(file);

  newImage.style.width = "70%";
  newImage.style.height = "70%";
  newImage.style.visibility = "hidden"; //버튼을 누르기 전까지는 이미지 숨기기
  newImage.style.objectFit = "contain";

  var container = document.getElementById("image-show");
  container.appendChild(newImage);
}

function readImage(input) {
  
  // 인풋 태그에 파일이 있는 경우
  if(input.files && input.files[0]) {

      // 이미지 파일인지 검사 (생략)

      // FileReader 인스턴스 생성
      const reader = new FileReader()

   // 이미지가 로드가 된 경우
      reader.onload = e => {
       const previewImage = document.getElementById("preview-image")
       previewImage.src = e.target.result
   }

      // reader가 이미지 읽도록 하기
  reader.readAsDataURL(input.files[0])
  }
}

// input file에 change 이벤트 부여
const inputImage = document.getElementById("chooseFile")
inputImage.addEventListener("change", e => {
  readImage(e.target)
})
