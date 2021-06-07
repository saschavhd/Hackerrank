function Rectangle(a, b) {
    var rect = {
        length: a,
        width: b,
        area: a * b,
        perimeter: (2*a) + (2*b)
    };
    return rect;
}
