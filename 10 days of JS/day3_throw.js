function isPositive(a) {
    try {
        if (a > 0) return "YES";
        if (a == 0) return "Zero Error";
        if (a < 0) return "Negative Error"
    }
    catch {
        return a
    }
}
