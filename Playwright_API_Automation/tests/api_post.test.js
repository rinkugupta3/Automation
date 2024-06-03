import { test, expect } from "@playwright/test";
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