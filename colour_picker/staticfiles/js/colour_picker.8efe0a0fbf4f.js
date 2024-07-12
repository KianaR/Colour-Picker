document.addEventListener('DOMContentLoaded', function () {
    form = document.getElementById("upload-form");
    p_container = form.querySelector('p');
    p_container.classList.add("col-10", "p-container");

    img = document.getElementById("img-preview");
    if (img.src){
        img.addEventListener('click', function (e) {
            id = document.getElementById("img-id-hidden").textContent;

            bounds = this.getBoundingClientRect();
            var left = bounds.left;
            var top=bounds.top;
            var x = e.pageX - left;
            var y = e.pageY - top;
            var cw=this.clientWidth;
            var ch=this.clientHeight;
            var iw=this.naturalWidth;
            var ih=this.naturalHeight;
            
            var px=x/cw*iw
            var py=y/ch*ih

            // var px = e.pageX - this.offsetLeft;
            // var py = e.pageY - this.offsetTop;
            requestPxColour(id, px, py)
        });
    }
});

function requestPxColour(img_id, x, y){
    var csrftoken = Cookies.get("csrftoken");

    $.ajax({
        type: "POST",
        url: "/request-colour/",
        data: {
            "img_id": img_id,
            "x": x,
            "y": y,
            "csrfmiddlewaretoken": csrftoken
        },
        success: function(response) {
            resp = JSON.parse(response);
            document.getElementById("colour-code").textContent = `rgb(${resp["rgb"]})`;
            document.getElementById("colour-code-container").style.backgroundColor = `rgb(${resp["rgb"]})`;

            document.getElementById("rgb").textContent = `rgb(${resp["rgb"]})`;

            if(resp["hex"] != 0){document.getElementById("hex").textContent = resp["hex"];}

            for (let i=1; i<6; i++){
                const name="recent-"+i
                console.log(name)
                document.getElementById(name).textContent = `rgb(${resp["recents"][i][1]})`;
                document.getElementById(name).style.backgroundColor = `rgb(${resp["recents"][i][1]})`;
            }
        }
    })
}

function copyCode(id) {
    colour = document.getElementById(id).textContent;
    navigator.clipboard.writeText(colour);
    alert("Copied: " + colour);
}