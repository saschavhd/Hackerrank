class Polygon {
    constructor(sides) {
        this.sides = sides;
    }

    perimeter() {
        let per = 0,
        for (let i = 0; i < this.sides.length; i++) {
            per += this.sides[i];
        }
        return per;
    }
}
