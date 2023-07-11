export default defineEventHandler(async (event) => {
  const path = getRequestPath(event);
  const config = useRuntimeConfig();
  const password = config.unlockPassword;

  // if we are on the locked page and the query password is correct, redirect to the home page
  if (path.startsWith('/locked')) {
    const query = getQuery(event);
    if (query.password === password) {
      setCookie(event, 'dobrodelen_password', password);
      return sendRedirect(event, '/', 302);
    }
  }

  // we are either on the locked page with wrong password or any other page

  const cookies = parseCookies(event);
  if (cookies.dobrodelen_password === password) {
    // if we are on the locked page and the cookie password is correct, redirect to the home page
    if (path.startsWith('/locked')) {
      return sendRedirect(event, '/', 302);
    }
  } else {
    // if the cookie password is incorrect, redirect to the locked page
    if (!path.startsWith('/locked')) {
      return sendRedirect(event, '/locked', 302);
    }
  }
});
