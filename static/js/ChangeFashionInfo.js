function changeFashionInfo() {
  /*
    let a="./img/(116)IMG_1.jpg"
    let fashionstyle = document.getElementById("FashionStyleImg");
    fashionstyle.src=a

    let e=document.querySelector('#StyleName');
    e.innerHTML="바캉스스타일"
    document.getElementById('StyleName').classNmme="stylefont"

    let stylename = document.querySelector("#StyleName");

    
    let input_percent = 14
    percent.innerHTML= input_percent;

    let style_comnent = document.querySelector("#style_comnent");

    let input_style_comnent = "바캉스는 좋아요~"
    style_comnent.innerHTML= input_style_comnent; 
    */
  const fileCheck = document.getElementById("chooseFile").value;
  if (!fileCheck) {
    alert("이미지를 업로드해 주세요.");
    return false;
  }
}
