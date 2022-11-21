const toggleStatus = (token) => {
    $.post("/token/toggle/", {
        token,
    },
    (data, status) => {
        $(`#status-${token}`).toggleClass("bg-red-400");
        $(`#status-${token}`).toggleClass("bg-green-400");

        if($(`#status-${token}`).hasClass("bg-red-400")){
            $(`#status-${token}`).html("Invalid");
        }else{
            $(`#status-${token}`).html("Valid");
        }
    });
}

const determineColor = (status) => {
    return status ? "bg-red-400" : "bg-green-400";
}

const determineStatus = (status) => {
    return status ? "Invalid" : "Valid";
}

const makeTr = (data) => {
    return `
    <tr class="text-center">
        <td class="border-r-2 border-l-2 border-b-2 border-russian-violet">${data.npm}</td>
        <td class="border-r-2 border-l-2 border-b-2 border-russian-violet">${data.name}</td>
        <td class="border-r-2 border-l-2 border-b-2 border-russian-violet">${data.token}</td>
        <td class="border-r-2 border-b-2 p-2 border-russian-violet ">
            <div class="flex justify-center gap-4">
                <p id="status-${data.token}" class="py-1 px-2 w-16 text-center ${determineColor(data.used)} rounded-3xl">${determineStatus(data.used)}</p>
                <button class="py-1 px-2 bg-liberty text-white hover:bg-blue-400 rounded-lg" onClick="toggleStatus('${data.token}')">Change</button>
            </div>
        </td>
    </tr>`;
}

$(document).ready(() => {
    $.get("/token/all/", (data) => {
        for(var i = 0; i < data.tokenList.length; i++){
            $("#token-table").append(makeTr(data.tokenList[i]));
        }
    })
});