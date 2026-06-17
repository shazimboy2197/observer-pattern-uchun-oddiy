# Observer pattern uchun oddiy misol

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


class Observer:
    def update(self, message):
        pass


class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Observer: Received message - {message}")


class ConcreteObserver2(Observer):
    def update(self, message):
        print(f"Observer2: Received message - {message}")


subject = Subject()

observer1 = ConcreteObserver()
observer2 = ConcreteObserver2()

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Hello, observers!")
subject.detach(observer2)

subject.notify("Hello, observers!")
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. `Subject` klassi - bu ob'ektlar uchun asosiy klass bo'lib, u ob'ektlarni ro'yxatga qo'shish, ro'yxatdan olib tashlash va ob'ektlarga xabar yuborish uchun metodlar beradi.
2. `Observer` klassi - bu ob'ektlar uchun asosiy klass bo'lib, u ob'ektlar uchun yangi metodlar beradi.
3. `ConcreteObserver` klassi - bu `Observer` klassidan meros qabul qilgan klass bo'lib, u yangi metodlarni implement qiladi.
4. `ConcreteObserver2` klassi - bu `Observer` klassidan meros qabul qilgan klass bo'lib, u yangi metodlarni implement qiladi.
5. `subject` ob'ekti - bu `Subject` klassidan meros qabul qilgan ob'ekt bo'lib, u ob'ektlarni ro'yxatga qo'shish, ro'yxatdan olib tashlash va ob'ektlarga xabar yuborish uchun metodlar beradi.
6. `observer1` va `observer2` ob'ektlari - bu `Observer` klassidan meros qabul qilgan ob'ektlar bo'lib, u yangi metodlarni implement qiladi.
7. `subject.attach(observer1)` - bu `observer1` ob'ekti ro'yxatga qo'shiladi.
8. `subject.attach(observer2)` - bu `observer2` ob'ekti ro'yxatga qo'shiladi.
9. `subject.notify("Hello, observers!")` - bu ob'ektlarga xabar yuboriladi.
10. `subject.detach(observer2)` - bu `observer2` ob'ekti ro'yxatdan olib tashlanadi.
11. `subject.notify("Hello, observers!")` - bu ob'ektlarga xabar yuboriladi.
