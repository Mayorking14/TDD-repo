let switchPower = false;
let temperature = 24;

function power(){
    return switchPower;
}


function toggleButton(){
    
    switchPower = !switchPower;

}

function currentTemperature(){
    return temperature
}

function increaseButton(){
    if(switchPower === false) Error("Ac is not on");
    if(temperature < 16) Error("Ac connot be higher than this");
    temperature--;
   
}

function decreaseButton(){
    if (switchPower) Error('AC is not on');
     if(temperature > 32) Error('AC cannot be lower than this')    
    temperature++;
}

module.exports = {power, toggleButton, currentTemperature, increaseButton, decreaseButton};
