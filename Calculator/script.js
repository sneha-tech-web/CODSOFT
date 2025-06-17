let display = document.getElementById("display");

function appendValue(value) {
  display.value += value;
}

function clearDisplay() {
  display.value = "";
}

function deleteLast() {
  display.value = display.value.slice(0, -1);
}

function calculate() {
  try {
    // Replace symbols if using unicode (e.g., × or ÷)
    let result = display.value.replace(/×/g, '*').replace(/÷/g, '/').replace(/−/g, '-');
    display.value = eval(result);
  } catch {
    display.value = "Error";
  }
}