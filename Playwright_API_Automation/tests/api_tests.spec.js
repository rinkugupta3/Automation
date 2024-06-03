// https://playwright.dev/docs/api-testing#writing-api-test
// https://playwright.dev/docs/api/class-apirequestcontext
// https://playwright.dev/docs/api/class-response#methods
// https://playwright.dev/docs/api/class-apiresponseassertions
// https://reqres.in/

import { test, expect } from "@playwright/test";

// Run below command "npx playwright test --ui" to execute the test
//API - GET Request - 200 OK - https://reqres.in

test("API Get Request", async ({ request }) => {
  const response = await request.get("https://reqres.in/api/users/2");

  expect(response.status()).toBe(200);

  const text = await response.text();
  expect(text).toContain("Janet");

  console.log(await response.json());
});

//API - POST Request - 201 Created - https://reqres.in
test("API Post Request", async ({ request }) => {
  const response = await request.post("https://reqres.in/api/users", {
    data: {
      name: "Dhiraj",
      job: "learning",
    },
  });
  expect(response.status()).toBe(201);

  const text = await response.text();
  expect(text).toContain("Dhiraj");

  console.log(await response.json());
});

//API - PUT Request - 200 Created - https://reqres.in
test("API Put Request", async ({ request }) => {
    const response = await request.put("https://reqres.in/api/users/2", {
      data: {
        name: "Dhiraj",
        job: "learning",
      },
    });
    expect(response.status()).toBe(200);
  
    const text = await response.text();
    expect(text).toContain("Dhiraj");
  
    console.log(await response.json());
  });

//API - DELETE Request - 204 No Content - https://reqres.in

test("API Delete Request", async ({ request }) => {
    const response = await request.delete("https://reqres.in/api/users/2");
  
    expect(response.status()).toBe(204);

  });