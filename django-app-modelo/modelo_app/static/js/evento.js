document.addEventListener("DOMContentLoaded", function () {
    const button = document.querySelector("#create-event-button");
    const form = document.querySelector("#eventoForm");
    const message = document.querySelector("#message");
    const eventosTable = document.querySelector("#eventosTable");
    const csrfToken = document.querySelector("#csrf_token").value;

    button.addEventListener("click", async function (event) {
        event.preventDefault(); 

        const name = document.querySelector("#name").value.trim();
        const fecha_inicio = document.querySelector("#fecha_inicio").value;
        const fecha_fin = document.querySelector("#fecha_fin").value;
        const localidad = document.querySelector("#localidad").value;


        if (!name || !fecha_inicio || !fecha_fin || !localidad) {
            message.innerText = "Todos los campos son obligatorios.";
            message.style.color = "red";
            return;
        }

        const today = new Date().toISOString().split("T")[0];
        if (fecha_inicio < today) {
            message.innerText = "La fecha de inicio no puede ser anterior a hoy.";
            message.style.color = "red";
            return;
        }
        if (fecha_fin < fecha_inicio) {
            message.innerText = "La fecha de fin no puede ser menor que la de inicio.";
            message.style.color = "red";
            return;
        }


        const data = {
            name: name,
            fecha_inicio: fecha_inicio,
            fecha_fin: fecha_fin,
            localidad: localidad
        };


        try {
            const response = await fetch("/ruta-para-crear-evento/", {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();

            if (result.status === "success") {
                message.innerText = "Evento creado con éxito.";
                message.style.color = "green";

                
                let newRow = eventosTable.insertRow();
                newRow.innerHTML = `<td>${result.evento.name}</td>
                                    <td>${result.evento.fecha_inicio}</td>
                                    <td>${result.evento.fecha_fin}</td>
                                    <td>${result.evento.localidad}</td>`;

                form.reset(); 
            } else {
                message.innerText = "Error: " + result.message;
                message.style.color = "red";
            }
        } catch (error) {
            message.innerText = "Error en la solicitud.";
            message.style.color = "red";
            console.error(error);
        }
    });
});
