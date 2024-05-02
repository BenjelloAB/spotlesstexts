console.log("Hello");



$(document).ready(function() {
  $('#lod').show(); // show the loading animation when the page loads
});

$(window).on('load', function() {
  $('#lod').fadeOut('slow'); // hide the loading animation when the page stops loading
})



// const input = document.querySelector('input[type="file"]');
const input = document.getElementById("up");
if (input) {
  input.addEventListener("change", () => {
    const file = input.files[0];
    const allowedExtensions = /(\.xlsx)$/i;
    if (!allowedExtensions.exec(file.name)) {
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Invalid file type. Only .xlsx files are allowed.',

      });
      input.value = "";
      return false;
    }
    // continue with file upload
  });
}

const realFileBtn = document.getElementById("up");
const customText = document.getElementById("cutosm_text");

if (realFileBtn) {
  realFileBtn.addEventListener("change", () => {
    if (realFileBtn.value) {
      customText.innerHTML = realFileBtn.value;
    }
    // ? ..value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)
    else {
      customText.innerHTML = "No file chosen yet ";
    }
  });
}


const cpButton = document.getElementById("copyButton");
const clButton = document.getElementById("clearButton");
const textArea = document.getElementById("outputTextarea");
const textInput = document.getElementById("inputTextarea");
if (cpButton) {
  cpButton.addEventListener("click", () => {
    textArea.select();
    document.execCommand("copy");
    textArea.classList.add("active");
    window.getSelection().removeAllRanges();
    setTimeout(() => {
      textArea.classList.remove("active");
    }, 1000);
  });
}

if (textInput) {
  textInput.addEventListener("keyup", () => {
    console.log(textInput);
    console.log(textInput.value);
    if (textInput.value.length > 0) {
      clButton.classList.remove("hidden");
    }
    if (textInput.value.length < 0) {
      clButton.classList.add("hidden");
    }
  });
}


// !------------inputs check excel ------------------


var checked = false;

// Get all input radio and checkboxes
var inputs = document.querySelectorAll('input[type="radio"], input[type="checkbox"]');
var formExcel = document.getElementById("formExcel");
if (formExcel) {
  formExcel.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!realFileBtn.value) {
      // If no file selected, display a warning message
      // alert('Please select a file to upload.');
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Please select a file to upload.',

      });
      return;
    } else {
      for (var i = 0; i < inputs.length; i++) {
        // If any input element is checked, set checked to true and break out of the loop
        if (inputs[i].checked) {
          checked = true;
          break;
        }
      }
      // Check if at least one input element is checked
      if (checked) {
        formExcel.submit();
      } else {
        // alert("No input elements are checked.");
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: 'Please check at least one option',

        });
      }
    }

  });
}







if (document.getElementById("clearButton")) {
  document.getElementById("clearButton").addEventListener("click", () => {
    document.getElementById("inputTextarea").value = "";
    clButton.classList.add("hidden");
  });
}

// !-----Menu profile -----
const menu = document.querySelector("#meh .menu");
const hh = document.querySelector(".HH");
document.onclick = function (e) {
  if (!e.target.classList.contains("HH")) {
    menu.classList.remove("active");
  } else {
    menu.classList.toggle("active");
  }
};

$('#preloader').hide();
// !------------FRENCH----------
$(document).on("submit", "#formFr", function (e) {
  // ? prevent the page from reloading:
  e.preventDefault();
  if (
    $('input[type="radio"]:checked, input[type="checkbox"]:checked').length > 0
  ) {
    $('#preloader').show();
    // at least one radio button or checkbox is checked
    var formData = {};

    // Get the value of the text input
    formData["text_input"] = $("#inputTextarea.textarea1Fr").val();

    // Create an empty array to hold the selected values
    var selectedValues = [];

    // Loop through all the checkboxes and radio buttons in the form
    $(
      'input[type="checkbox"][name="option"], input[type="radio"][name="option"]'
    ).each(function () {
      // Check if the checkbox or radio button is checked or selected
      if ($(this).is(":checked")) {
        // If it is, push its value into the selectedValues array
        selectedValues.push($(this).val());
      }
    });

    // Add the selectedValues array to the formData object
    formData["selected_values"] = selectedValues;
    $.ajax({
      type: "POST",
      url: "/french_bib_handle/",
      data: formData,
      headers: {
        "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
      },
      success: (data) => {
        $('#preloader').hide();
        console.log(data);
        console.log(data.string);
        string = data.string;
        $("#outputTextarea.textarea2Fr").text(string);
      },
      error: (err) => {
        $('#preloader').hide();
        console.log(err);
      },
    });
    $("html, body").animate(
      {
        scrollTop: 0,
      },
      1000
    );
  } else {
    // no radio buttons or checkboxes are checked
    // alert("Please check at least one option");
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: 'Please check at least one option',

    });
  }
});
// !--------ARABIC--------------
$(document).on("submit", "#formAr", function (e) {
  // ? prevent the page from reloading:
  e.preventDefault();
  if (
    $('input[type="radio"]:checked, input[type="checkbox"]:checked').length > 0
  ) {
    $('#preloader').show();
    // at least one radio button or checkbox is checked
    var formData = {};

    // Get the value of the text input
    formData["text_input"] = $("#inputTextarea.textarea1Ar").val();

    // Create an empty array to hold the selected values
    var selectedValues = [];

    // Loop through all the checkboxes and radio buttons in the form
    $(
      'input[type="checkbox"][name="option"], input[type="radio"][name="option"]'
    ).each(function () {
      // Check if the checkbox or radio button is checked or selected
      if ($(this).is(":checked")) {
        // If it is, push its value into the selectedValues array
        selectedValues.push($(this).val());
      }
    });

    // Add the selectedValues array to the formData object
    formData["selected_values"] = selectedValues;
    $.ajax({
      type: "POST",
      url: "/arabic_bib_handle/",
      data: formData,
      headers: {
        "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
      },
      success: (data) => {
        $('#preloader').hide();
        console.log(data);
        console.log(data.string);
        string = data.string;
        $("#outputTextarea.textarea2Ar").text(string);
      },
      error: (err) => {
        $('#preloader').hide();
        console.log(err);
      },
    });
    $("html, body").animate(
      {
        scrollTop: 0,
      },
      1000
    );
  } else {
    // no radio buttons or checkboxes are checked
    // alert("Please check at least one option");
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: 'Please check at least one option',

    });
  }
});
// !----------ENGLISH------------

$(document).on("submit", "#formEng", function (e) {
  // ? prevent the page from reloading:
  e.preventDefault();
  if (
    $('input[type="radio"]:checked, input[type="checkbox"]:checked').length > 0
  ) {
    $('#preloader').show();
    // at least one radio button or checkbox is checked
    var formData = {};

    // Get the value of the text input
    formData["text_input"] = $("#inputTextarea.textarea1Eng").val();

    // Create an empty array to hold the selected values
    var selectedValues = [];

    // Loop through all the checkboxes and radio buttons in the form
    $(
      'input[type="checkbox"][name="option"], input[type="radio"][name="option"]'
    ).each(function () {
      // Check if the checkbox or radio button is checked or selected
      if ($(this).is(":checked")) {
        // If it is, push its value into the selectedValues array
        selectedValues.push($(this).val());
      }
    });

    // Add the selectedValues array to the formData object
    formData["selected_values"] = selectedValues;
    $.ajax({
      type: "POST",
      url: "/english_bib_handle/",
      data: formData,
      headers: {
        "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
      },
      success: (data) => {
        $('#preloader').hide();
        console.log(data);
        console.log(data.string);
        string = data.string;
        $("#outputTextarea.textarea2Eng").text(string);
      },
      error: (err) => {
        $('#preloader').hide();
        console.log(err);
      },
    });
    $("html, body").animate(
      {
        scrollTop: 0,
      },
      1000
    );
  } else {
    // no radio buttons or checkboxes are checked
    // alert("Please check at least one option");
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: 'Please check at least one option',

    });
  }
});
// !----------DARIJA------------
$(document).on("submit", "#formDr", function (e) {
  // ? prevent the page from reloading:
  e.preventDefault();
  if (
    $('input[type="radio"]:checked, input[type="checkbox"]:checked').length > 0
  ) {
    $('#preloader').show();
    // at least one radio button or checkbox is checked
    var formData = {};

    // Get the value of the text input
    formData["text_input"] = $("#inputTextarea.textarea1Dr").val();

    // Create an empty array to hold the selected values
    var selectedValues = [];

    // Loop through all the checkboxes and radio buttons in the form
    $(
      'input[type="checkbox"][name="option"], input[type="radio"][name="option"]'
    ).each(function () {
      // Check if the checkbox or radio button is checked or selected
      if ($(this).is(":checked")) {
        // If it is, push its value into the selectedValues array
        selectedValues.push($(this).val());
      }
    });

    // Add the selectedValues array to the formData object
    formData["selected_values"] = selectedValues;
    $.ajax({
      type: "POST",
      url: "/darija_bib_handle/",
      data: formData,
      headers: {
        "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
      },
      success: (data) => {
        $('#preloader').hide();
        console.log(data);
        console.log(data.string);
        string = data.string;
        $("#outputTextarea.textarea2Dr").text(string);
      },
      error: (err) => {
        $('#preloader').hide();
        console.log(err);
      },
    });
    $("html, body").animate(
      {
        scrollTop: 0,
      },
      1000
    );
  } else {
    // no radio buttons or checkboxes are checked
    // alert("Please check at least one option");
    Swal.fire({
      icon: 'error',
      title: 'Oops...',
      text: 'Please check at least one option',

    });
  }
});

