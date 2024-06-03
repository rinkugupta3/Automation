import { test, expect } from "@playwright/test";
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