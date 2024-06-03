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