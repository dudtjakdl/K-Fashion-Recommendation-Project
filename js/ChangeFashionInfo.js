function changeFashionInfo(){
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
    document.getElementById('loading').style="display:block"
    window.setTimeout(
      () =>{
        //결과div 반환
    let analysis_div = document.getElementById('analysis');
    analysis_div.style="display:block"

    //로딩화면 삭제
    let loading=document.getElementById('loading');
    loading.style="display:none;"
      } , 4000);
    
  }