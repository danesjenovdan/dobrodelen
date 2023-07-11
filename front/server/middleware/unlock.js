export default defineEventHandler(async (event) => {
  const path = getRequestPath(event);
  const config = useRuntimeConfig();
  const password = config.unlockPassword;

  if (path.startsWith('/locked')) {
    const query = getQuery(event);
    if (query.password === password) {
      setCookie(event, 'dobrodelen_password', password);
      return sendRedirect(event, '/', 302);
    }
  } else {
    const cookies = parseCookies(event);
    if (cookies.dobrodelen_password !== password) {
      return sendRedirect(event, '/locked', 302);
    }
  }
});
