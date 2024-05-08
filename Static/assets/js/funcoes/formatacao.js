
function Moeda(input) {

    let valor = input.value;

    const formatter = new Intl.NumberFormat('pt-BR', {
        minimumFractionDigits: 2
    });

    input.value = formatter.format(valor);

}

function MoedaKeyUp(input) {

    let valor = input.value;


    valor = valor + '';
    valor = parseInt(valor.replace(/[\D]+/g, ''));
    valor = valor + '';
    valor = valor.replace(/([0-9]{2})$/g, ",$1");

    if (valor.length > 6) {
        valor = valor.replace(/([0-9]{3}),([0-9]{2}$)/g, ".$1,$2");
    }

    valor = parseFloat(valor).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');

    input.value = valor;

}

function Estoque(input) {

    let value = input.value;
    value = value.replace(/[^\d.]/g, '');

    let partes = value.split('.');

    if (partes.length > 1) {
        partes[1] = partes[1].slice(0, 3);
        value = partes.join('.');
    }

    input.value = value;
}

