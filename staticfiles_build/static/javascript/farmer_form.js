
    function validateForm() {
        // Get form input values
        var fatherName = document.getElementById("fatherName").value;
        var mobileNumber = document.getElementById("mobileNumber").value;
        var mailId = document.getElementById("mailId").value;
        var aadhaarNumber = document.getElementById("aadhaarNumber").value;
        var panNumber = document.getElementById("panNumber").value;
        var landArea = document.getElementById("landArea").value;
        var accountNumber = document.getElementById("accountNumber").value;
        var ifscCode = document.getElementById("ifscCode").value;
        var bankName = document.getElementById("bankName").value;
        var loanDetails = document.getElementById("loanDetails").value;
        var investmentSize = document.getElementById("investmentSize").value;
        var jobCardNumber = document.getElementById("jobCardNumber").value;
        var farmerName1 = document.getElementById("farmerName1").value;
        var mobileNumber1 = document.getElementById("mobileNumber1").value;
        var land1 = document.getElementById("land1").value;
        var anotherFarmerName = document.getElementById("anotherFarmerName").value;
        var mobileNumber2 = document.getElementById("mobileNumber2").value;
        var landArea2 = document.getElementById("landArea2").value;

        // Define validation patterns
        var mobileRegex = /^[0-9]{10}$/;
        var aadhaarRegex = /^[0-9]{12}$/;
        var panRegex = /^[A-Z]{5}[0-9]{4}[A-Z]$/;
        var ifscRegex = /^[A-Z]{4}0[A-Z0-9]{6}$/;

        // Validate each field
        if (fatherName.trim() === "") {
            alert("Father's Name is required.");
            return false;
        }

        if (!mobileRegex.test(mobileNumber)) {
            alert("Please enter a valid 10-digit Mobile Number.");
            return false;
        }

        if (!aadhaarRegex.test(aadhaarNumber)) {
            alert("Please enter a valid 12-digit Aadhaar Card Number.");
            return false;
        }

        if (!panRegex.test(panNumber)) {
            alert("Please enter a valid PAN Card Number (e.g., ABCDE1234F).");
            return false;
        }

        if (isNaN(landArea) || landArea <= 0) {
            alert("Please enter a valid Land Area (greater than 0).");
            return false;
        }

        if (accountNumber.trim() === "") {
            alert("Account Number is required.");
            return false;
        }

        if (!ifscRegex.test(ifscCode)) {
            alert("Please enter a valid IFSC Code.");
            return false;
        }

        if (bankName.trim() === "") {
            alert("Bank Name is required.");
            return false;
        }

        if (loanDetails.trim() === "") {
            alert("Loan Details is required.");
            return false;
        }

        if (isNaN(investmentSize) || investmentSize <= 0) {
            alert("Please enter a valid First Time Investment Size (greater than 0).");
            return false;
        }

        if (jobCardNumber.trim() === "") {
            alert("Job Card Number is required.");
            return false;
        }

        // if (farmerName1.trim() === "") {
        //     alert("Farmer Name 1 is required.");
        //     return false;
        // }

        // if (!mobileRegex.test(mobileNumber1)) {
        //     alert("Please enter a valid 10-digit Mobile Number 1.");
        //     return false;
        // }

        // if (isNaN(land1) || land1 <= 0) {
        //     alert("Please enter a valid Land Area 1 (greater than 0).");
        //     return false;
        // }

        // if (anotherFarmerName.trim() === "") {
        //     alert("Another Farmer Name is required.");
        //     return false;
        // }

        // if (!mobileRegex.test(mobileNumber2)) {
        //     alert("Please enter a valid 10-digit Mobile Number 2.");
        //     return false;
        // }

        // if (isNaN(landArea2) || landArea2 <= 0) {
        //     alert("Please enter a valid Land Area 2 (greater than 0).");
        //     return false;
        // }

        // If all validations pass, the form will be submitted
        return true;
    }
