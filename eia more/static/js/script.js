function changeGraph() {
    var selector = document.getElementById('graphSelector');
    var image = document.getElementById('graphImage');
    image.src = selector.value;
    console.log("Image src: " + image.src);
}
