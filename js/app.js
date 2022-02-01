$(document).foundation()

document.getElementById('date').innerHTML = Date()

/* Function to return random number between 0 and 100 */
function myRandomNum(){
    var max = 101;
    let min = 0;
    let result = Math.floor(Math.random() * (max - min)) + min;
    document.getElementById('randomResult').innerHTML = result;
    // for(var i = 0; i < max; i++){
    //     console.log(i);
    // }
    // console.log("i: " + i);
}
