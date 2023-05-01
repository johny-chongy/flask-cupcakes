const BASE_URL = "/api/cupcakes";

const $addCupcakeForm = $("#addCupcake");
const $cupcakeList = $("#cupcakeList");

/**
 * Adding the form data to the database and show it to the page as a list
 */
async function handleNewCupcake(evt) {
  evt.preventDefault();

  let flavor = $("#flavor").val(); //FIXME: const everything
  let size = $("#size").val();
  let rating = $("#rating").val();
  let image_url = $("#imageUrl").val();

  let cupcake = { flavor, size, rating, image_url };

  let response = await axios.post(BASE_URL, cupcake);

  let cupcakeResponse = response.data.cupcake;

  //TODO: might be more scalable if separate out
  //FIXME: get

  $cupcakeList.append(
    `<li><a href="${BASE_URL}/${cupcakeResponse.id}">${cupcakeResponse.flavor}</a></li>`
  );
}

$addCupcakeForm.on("submit", handleNewCupcake);
