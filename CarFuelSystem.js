let defaultState = false
const fuelCapacity = 50
const fuelEfficiency = 5


function carDefault(){
    return defaultState
}

function ignition(){
    defaultState = !defaultState
}

function refuel(fuelGuage){
    if (fuelGuage === 0 || fuelGuage < fuelCapacity){
        return true
    }
}

function canBeDriven(currentGuage){
    let currentGuage = fuelCapacity - fuelConsumed
    if (ignition && currentGuage != 0){
        return true
    }
    
}


function getCurrentFuelState(distance){
    let fuelConsumed = distance / fuelEfficiency
    if(ignition()){
        let fuelState = fuelCapacity - fuelConsumed 
        return fuelState
    }
}


module.exports = {carDefault,ignition,refuel,canBeDriven,getCurrentFuelState};