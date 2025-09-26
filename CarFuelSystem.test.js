const {carDefault,ignition,refuel,canBeDriven,getCurrentFuelState} = require('../src/CarFuelSystem');

describe('Test for my car should be off', ()=>{
    test('should be off', ()=>{
        expect(carDefault()).toBe(false);
    });

    test('test that car can start', ()=>{
        expect(carDefault()).toBe(false);
        ignition()
        expect(carDefault()).toBe(true);
    })

    test('test that car can be stopped',()=>{
        ignition()
        expect(carDefault()).toBe(false);
    })

    test('test that car can be refueled', () => {
        carDefault()
        expect(refuel(45)).toBe(true)
    })

    test('test that i cannot refuel if tank is full', ()=> {
        ignition()
        expect(refuel(50)).toBe(false)
    })

    test('test that car can be driven', ()=>{
        ignition()
        expect(canBeDriven(25)).toBe(true)
    })

    test('test that car cannot be driven when off', ()=>{
        ignition()
        expect(carDefault()).toBe(false)
        expect(canBeDriven(23)).toBe(false)
    })

    test('test that car cannot be driven if guage is 0', ()=>{
        ignition()
        expect(carDefault()).toBe(true)
        expect(canBeDriven(0)).toBe(false)

    })

    test('test the current fuel state of the car', ()=>{
        expect(carDefault()).toBe(true)
        expect(getCurrentFuelState(5)).toBe(49)

    })

    test('test if car is running or not', ()=>{
        
    })
});