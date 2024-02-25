class Students {
  constructor(ID, Familiya, Ismi, Guruhi) {
    this.ID = ID;
    this.Familiya = Familiya;
    this.Ismi = Ismi;
    this.Guruhi = Guruhi;
    this.Tsana = [];
  }

  inputS(ocenka) {
    this.Tsana.push(ocenka);
  }

  shows() {
    console.log(`ID: ${this.ID}`);
    console.log(`Фамилия: ${this.Familiya}`);
    console.log(`Имя: ${this.Ismi}`);
    console.log(`Группа: ${this.Guruhi}`);
    console.log(`Оценки: ${this.Tsana.join(', ')}`);
  }
}

// Пример использования класса:
let student = new Students(1, "Иванов", "Иван", "Группа1");
student.inputS(5);
student.inputS(4);
student.inputS(3);

student.shows();
