console.log("hello world");
const firstmodal = document.getElementById("firstmodal");

$.ajax({
    type: 'GET',
    url: 'data-json',
    success: function (response){
        console.log(response)
        const data = JSON.parse(response.data)
        console.log(data)
        data.forEach(element => {
            console.log(element.fields)
            firstmodal.innerHTML += `
                <tr>
                    <td>${element.pk}</td>
                    <td>${element.fields.items}</td>
                    <td>${element.fields.stockImg}</td>
            `
        });
    },
    error: function (error){
        console.log(error);
    }

    
})