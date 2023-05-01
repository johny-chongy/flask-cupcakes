const BASE_URL = "/api/cupcakes";

const $addCupcakeForm = $("#addCupcake");
const $cupcakeList = $("#cupcakeList");

startView();

async function startView() {
  let response = await axios.get(BASE_URL)

  for (let cupcakeResponse of response.data.cupcakes) {
    appendCupcaketoList(cupcakeResponse);
  }
}


/**
 * Adding the form data to the database and show it to the page as a list
 */
async function handleNewCupcake(evt) {
  evt.preventDefault();

  const flavor = $("#flavor").val();
  const size = $("#size").val();
  const rating = $("#rating").val();
  const image_url = $("#imageUrl").val();

  let cupcake = { flavor, size, rating, image_url };
  let response = await axios.post(BASE_URL, cupcake);
  let cupcakeResponse = response.data.cupcake;

  appendCupcaketoList(cupcakeResponse);
}



/** Adds cupcake to DOM visually from JSON response value */
function appendCupcaketoList(cupcakeResponse) {
  $cupcakeList.append(
    `<li><a href="${BASE_URL}/${cupcakeResponse.id}">${cupcakeResponse.flavor}</a></li>`
    );
  }


$addCupcakeForm.on("submit", handleNewCupcake);