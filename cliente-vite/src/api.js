const BASE_URL = 'https://parallelum.com.br/fipe/api/v1';

export async function getMarcas(tipo) {
  const res = await fetch(`${BASE_URL}/${tipo}/marcas`);
  return res.json();
}

export async function getModelos(tipo, marca) {
  const res = await fetch(`${BASE_URL}/${tipo}/marcas/${marca}/modelos`);
  return res.json();
}

export async function getAnos(tipo, marca, modelo) {
  const res = await fetch(`${BASE_URL}/${tipo}/marcas/${marca}/modelos/${modelo}/anos`);
  return res.json();
}

export async function getVeiculo(tipo, marca, modelo, ano) {
  const res = await fetch(`${BASE_URL}/${tipo}/marcas/${marca}/modelos/${modelo}/anos/${ano}`);
  return res.json();
}
