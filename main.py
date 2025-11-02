// Main.java
public class Main {
    
    // v1.0.0 - Наисание Hello world
    public static void printHelloWorld() {
        System.out.println("Hello, World");
    }
    
    // v1.1.0 - написание как тебя зовут 
    public static void askName() {
        System.out.println("Как тебя зовут");
    }
    
    // v1.1.1 - Баг: деление на ноль (оригинальная версия с багом)
    public static double calculateWithBug() {
        double result = 10 / 0;  // БАГ: деление на ноль
        return result;
    }
    
    // v1.1.1 - Исправленная версия
    public static double calculateFixed() {
        double result = 10 / 2;  // Исправлено: деление на 2
        return result;
    }
    
    // v1.2.0 - Новый функционал
    public static void askAge() {
        System.out.println("сколько тебе лет ");
    }
    
    public static void main(String[] args) {
        // Запуск всех версий функциональности
        printHelloWorld();      // v1.0.0
        askName();              // v1.1.0
        
        // Демонстрация бага и исправления
        try {
            calculateWithBug(); // v1.1.1 (баг)
        } catch (ArithmeticException e) {
            System.out.println("Обнаружен баг: " + e.getMessage());
        }
        
        double result = calculateFixed(); // v1.1.1 (исправлено)
        System.out.println("Исправленный результат: " + result);
        
        askAge(); // v1.2.0
    }
}
