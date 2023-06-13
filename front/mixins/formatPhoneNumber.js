import _ from 'lodash';

const AREA_CODES = {
  mobile: [
    '030',
    '040',
    '068',
    '069',
    '031',
    '041',
    '051',
    '071',
    '065',
    '070',
    '064',
    '065',
  ],
  special: ['080', '089', '090'],
  voip: ['059', '081', '082', '083'],
  landline: ['01', '02', '03', '04', '05', '07'],
};

const AREA_CODE_FORMATTERS = {
  mobile(n) {
    if (n.length === 9) {
      return `${n.slice(0, 3)} ${n.slice(3, 6)} ${n.slice(6, 9)}`;
    }
  },
  special(n) {
    if (n.length === 9) {
      return `${n.slice(0, 3)} ${n.slice(3, 6)} ${n.slice(6, 9)}`;
    }
    if (n.length === 7) {
      return `${n.slice(0, 3)} ${n.slice(3, 5)} ${n.slice(5, 7)}`;
    }
  },
  voip(n) {
    if (n.length === 9) {
      return `${n.slice(0, 3)} ${n.slice(3, 5)} ${n.slice(5, 7)} ${n.slice(
        7,
        9,
      )}`;
    }
  },
  landline(n) {
    if (n.length === 9) {
      return `${n.slice(0, 2)} ${n.slice(2, 5)} ${n.slice(5, 7)} ${n.slice(
        7,
        9,
      )}`;
    }
  },
};

function getPlainNumber(phoneNumber) {
  const n = String(phoneNumber)
    .replace(/[^0-9]/g, '')
    .replace(/^386/g, '')
    .replace(/^00386/g, '');
  return n[0] === '0' ? n : `0${n}`;
}

function tryFormat(phoneNumber) {
  const type = _.keys(AREA_CODES).find((key) =>
    AREA_CODES[key].some((code) => phoneNumber.indexOf(code) === 0),
  );

  return AREA_CODE_FORMATTERS[type](phoneNumber) || phoneNumber;
}

export default {
  methods: {
    formatPhoneNumber(phoneNumber) {
      return tryFormat(getPlainNumber(phoneNumber));
    },
  },
};
