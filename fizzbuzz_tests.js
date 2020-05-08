// import the code to be tested
const { fizz } = require ('../fizzbuzz') // the "old" safe way to import stuff
    import { fizz } from '../fizzbuzz' //the "new" sexy way to import stuff (ES6+)


describe('A FizzBuzz program', () => {
    it('has a smoke test', () => {
        expect(true).toBe(true)
        expect(true).not.toBe(false)
})

    describe('A Fizz() function', () => {
        it('throws an error if there is no input', () => {
            expect(() => { fizz() }).toThrow()
            expect(() => { fizz(3) }).not.toThrow()
        })
    })
})