
const BASE_URL = '/api/cupcakes'

const $addCupcakeForm = $("#addCupcake")


async function handleNewCupcake(evt) {
  evt.preventDefault();

  let flavor = $('#flavor').val()
  let size = $('#size').val()
  let rating = $('#rating').val()
  let imageUrl = $('#imageUrl').val()

  console.log(flavor)

  let cupcake = {
    flavor:flavor,
    size:size,
    rating:rating,
    imageUrl:imageUrl}

  console.log(cupcake);

  // let response = await axios.post(
  //   BASE_URL,
  //   {data: cupcake},
  //   {headers: {
  //     'Content-Type':'application/json'
  //   }}
  // )

  // let response = await axios.post(
  //       BASE_URL,
  //       {headers: {
  //         'Content-Type':'application/json'
  //       }},
  //       {data: jsonInput},);

  // console.log(response);


}



$addCupcakeForm.addEventListener("submit", handleNewCupcake)