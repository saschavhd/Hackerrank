Rectangle.prototype.area = function() {
    return this.w * this.h;
}

class Square extends Rectangle {
    constructor(z) {
        super(z);
        this.w = z;
        this.h = z;
    }
}
